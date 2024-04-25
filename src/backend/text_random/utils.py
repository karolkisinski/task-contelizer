import random


class RandomizeText():
    @classmethod
    def process_file(cls, file, chunk_size=1024):
        processed_text = ""
        while True:
            chunk = file.read(chunk_size)
            if not chunk:
                break
            processed_text += cls.process_chunk(chunk.decode('utf-8'))
        return processed_text

    @classmethod
    def process_chunk(cls, chunk):
        processed_lines = []
        for line in chunk.split('\n'):
            processed_lines.append(cls.process_line(line))
        return '\n'.join(processed_lines)

    @classmethod
    def process_line(cls, line):
        words = line.split()

        processed_words = []
        for word in words:
            if len(word) > 3:
                word_list = list(word[1:-1])
                random.shuffle(word_list)
                processed_word = word[0] + ''.join(word_list) + word[-1]
                processed_words.append(processed_word)
            else:
                processed_words.append(word)
        return ' '.join(processed_words)
