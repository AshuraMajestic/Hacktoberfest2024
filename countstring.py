def count_words(text):
    """Counts the number of words in the text."""
    words = text.split()
    return len(words)

def count_sentences(text):
    """Counts the number of sentences in the text."""
    sentences = text.split('.')
    # Removing empty splits that may occur due to trailing periods.
    sentences = [s for s in sentences if s.strip() != ""]
    return len(sentences)

def count_paragraphs(text):
    """Counts the number of paragraphs in the text."""
    paragraphs = text.split('\n')
    # Removing empty splits that may occur due to extra newlines.
    paragraphs = [p for p in paragraphs if p.strip() != ""]
    return len(paragraphs)

def main():
    # Example text input
    text = """This is the first sentence. This is the second sentence.
    
    This is the first sentence of the second paragraph."""
    
    word_count = count_words(text)
    sentence_count = count_sentences(text)
    paragraph_count = count_paragraphs(text)
    
    print(f"Words: {word_count}")
    print(f"Sentences: {sentence_count}")
    print(f"Paragraphs: {paragraph_count}")

if __name__ == "__main__":
    main()
