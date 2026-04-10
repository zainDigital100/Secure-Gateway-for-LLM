from presidio_analyzer import AnalyzerEngine, PatternRecognizer, Pattern
from presidio_anonymizer import AnonymizerEngine

analyzer = AnalyzerEngine()
anonymizer = AnonymizerEngine()

api_key_pattern = Pattern(
    name="api_key_pattern", 
    regex=r"sk-[a-zA-Z0-9]{20,}", 
    score=0.8
)
api_key_recognizer = PatternRecognizer(
    supported_entity="API_KEY",
    patterns=[api_key_pattern],
    context=["key", "api", "token", "secret"]
)

cui_id_pattern = Pattern(
    name="cui_id_pattern", 
    regex=r"CUI-\d{5}-[A-Z]", 
    score=0.9
)
cui_id_recognizer = PatternRecognizer(
    supported_entity="INTERNAL_ID",
    patterns=[cui_id_pattern]
)

pk_phone_pattern = Pattern(
    name="pk_phone_pattern", 
    regex=r"((\+92)|(0))3\d{2}-?\d{7}", 
    score=0.85
)
pk_phone_recognizer = PatternRecognizer(
    supported_entity="PHONE_NUMBER",
    patterns=[pk_phone_pattern]
)

analyzer.registry.add_recognizer(api_key_recognizer)
analyzer.registry.add_recognizer(cui_id_recognizer)
analyzer.registry.add_recognizer(pk_phone_recognizer)

def analyze_pii(text):
    return analyzer.analyze(
        text=text, 
        language="en", 
        entities=["API_KEY", "INTERNAL_ID", "PHONE_NUMBER", "EMAIL_ADDRESS", "PERSON"]
    )

def mask_pii(text, results):
    result = anonymizer.anonymize(text=text, analyzer_results=results)
    return result.text