class GraphAdjList:  # Kelas untuk membuat graph menggunakan adjacency list
    def __init__(self, directed=False):  # Konstruktor: buat storage kosong untuk graph
        self.adj_list = {}  # Gunakan dictionary untuk menyimpan hubungan antar node
        self.directed = directed  # Simpan apakah graph directed (satu arah) atau tidak
    