class Mangga:
    # magic method
    def __init__(self, nama, jumlah):
        self.nama = nama
        self.jumlah = jumlah

    # repr biasanya digunakan pas debug
    # def __repr__(self):
    #     return "Mangga: {}".format(self.nama)

    # str digunakan ketika sudah launching
    def __str__(self):
        return "Mangga: {}".format(self.nama)

    # maghic method __*__
    def __add__(self, objek):
        return self.jumlah + objek.jumlah


Mama = Mangga("harum manis", 10)
Mama2 = Mangga("harum manis", 30)
print(Mama)
print(Mama + Mama2)

print(Mama2.__dict__)
