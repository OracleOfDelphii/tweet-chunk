import pyperclip

class Chunk:

    chunks : []

    def __len__(self):
        return len(self.chunks)

    def __getitem__(self, index):
        return self.chunks[index]

    def __init__(self, text):
        sp = text.split(" ")
        chunks = []
        i = 0
        chunk = ""
        for wd in sp:

            if len(wd) + len(chunk) + 6 <= 280:
                if chunk != "":
                    chunk = chunk + " " + wd
                else:

                    if i > 0:
                        chunk = f"/{i}\n" + chunk + wd
                    else:
                        chunk = chunk + wd

                    chunk = f"/{i}\n" + chunk + wd
            else:
                chunks = chunks + [chunk + "/ \n"]
                i += 1
                chunk = f"/{i}\n" + wd

        if chunks == []:
            chunks = chunks +  [chunk]

        if chunk != "":
            chunks = chunks + [chunk]
        self.chunks = chunks

    def get_chunk(self, i):
        return str(self.chunks[i])
