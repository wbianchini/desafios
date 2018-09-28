class StringManipulation:

    DEFAULT_LENGTH = 40

    def __init__(self):
        self.input_text = ""
        self.output_text = ""
        self.current_line = ""
        self.line_length_limit = self.DEFAULT_LENGTH

    def format(self):
        self.limit_line_length()

        return self.output_text

    def limit_line_length(self):
        input_words = self.input_text.split(" ")
        for word in input_words:
            if word.startswith("\n"):
                self.output_text += self.current_line
                self.current_line = word
            elif self.have_space_to_add(" " + word):
                self.current_line = self.concat_word(self.current_line, word)
            else:
                self.concat_new_line(word)

        self.concat_new_line("")

    def remove_paragraphs_at_end(self, input_text):
        if not input_text.endswith("\n") and not input_text.endswith("\r"):
            return input_text

        input_text = input_text[:-1]
        return self.remove_paragraphs_at_end(input_text)

    def have_space_to_add(self, word):
        return (len(self.current_line) + len(word)) <= self.line_length_limit

    def concat_word(self, line, word):
        if "" == line:
            line += word
        else:
            line += " " + word

        return line

    def check_tabs_to_apply(self, tabs_to_apply, length_words):
        if (tabs_to_apply / length_words) > 0:
            return tabs_to_apply / length_words
        return 1

    def concat_new_line(self, word):
        self.output_text += self.justify_text_line(self.current_line) + "\n"
        self.current_line = word

    def justify_text_line(self, line):
        tabs_to_apply = 0
        line = line.rstrip()

        line_length = len(line) - line.count("\n")

        if line_length < self.line_length_limit:
            tabs_to_apply = self.line_length_limit - line_length

        if tabs_to_apply <= 0:
            return line

        new_line = ""
        words = line.split(" ")
        tab_by_word = self.check_tabs_to_apply(tabs_to_apply, len(words))

        tabs_applied = 0
        for word in words:
            if (tabs_applied + tab_by_word) <= tabs_to_apply:
                word += (" " * tab_by_word)
                tabs_applied += tab_by_word
            new_line = self.concat_word(new_line, word)

        line = self.justify_text_line(new_line)
        return line

    def set_input_text(self, input_text):
        if input_text.endswith("\n"):
            input_text = self.remove_paragraphs_at_end(input_text)

        self.input_text = input_text.replace("\r", "").replace("\n", " \n")
