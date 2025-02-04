from deep_translator import GoogleTranslator

def translate_text(text, target_lang):
    try:
        translation = GoogleTranslator(source='auto', target=target_lang).translate(text)
        return translation
    except Exception as e:
        return f"Error: {e}"

def main():
    print("=== Simple Language Translator ===")
    text = input("Enter text to translate: ")
    dest_language = input("Enter target language code (e.g., 'es' for Spanish, 'fr' for French) or name: ")
    
    translated_text = translate_text(text, dest_language)
    print(f"\nTranslated Text: {translated_text}")

if __name__ == "__main__":
    main()