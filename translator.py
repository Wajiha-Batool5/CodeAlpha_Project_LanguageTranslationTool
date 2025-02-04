from googletrans import Translator

def translate_text(text, dest_language):
    translator = Translator()
    try:
        translation = translator.translate(text, dest=dest_language)
        return translation.text
    except Exception as e:
        return f"Error: {e}"

def main():
    print("=== Simple Language Translator ===")
    text = input("Enter text to translate: ")
    dest_language = input("Enter target language code (e.g., 'es' for Spanish, 'fr' for French): ")
    
    translated_text = translate_text(text, dest_language)
    print(f"\nTranslated Text: {translated_text}")

if __name__ == "__main__":
    main()