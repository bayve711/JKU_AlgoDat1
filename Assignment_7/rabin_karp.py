class RabinKarp:
    def search(self, pattern, text):
        if not pattern or not text:
            raise ValueError("Pattern or text is empty")

        output = []
        pat = len(pattern)
        orig_text = len(text)
        pat_hash = self.get_rolling_hash_value(pattern, "", None)
        text_hash = self.get_rolling_hash_value(text[:pat], "", None)

        for index in range(orig_text - pat + 1):
            if pat_hash == text_hash:
                if pattern == text[index:index + pat]:
                    output.append(index)

            if index < orig_text - pat:
                text_hash = self.get_rolling_hash_value(text[index + 1:index + pat + 1], text[index], text_hash)

        return output if output else None

    def get_rolling_hash_value(self, sequence, last_character, previous_hash):
        b = 29

        if previous_hash is None:
            val = 0
            for elem in sequence:
                val = (b * val + ord(elem))
        else:
            val = (previous_hash - ord(last_character) * (b ** (len(sequence) - 1))) * b + ord(sequence[-1])

        return val

