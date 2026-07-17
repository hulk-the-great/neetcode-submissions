class Codec:
    def encode(self, strs):
        encoded = ""

        for word in strs:
            encoded += str(len(word)) + "#" + word

        return encoded

    def decode(self, s):
        result = []
        i = 0

        while i < len(s):
            j = i

            # Find the separator #
            while s[j] != "#":
                j += 1

            # Length of the next word
            length = int(s[i:j])

            # Word starts after #
            word_start = j + 1
            word_end = word_start + length

            result.append(s[word_start:word_end])

            # Move i to the next encoded word
            i = word_end

        return result