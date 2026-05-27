class GraphAdjList:  # Kelas untuk membuat graph menggunakan adjacency list
    def __init__(self, directed=False):  # Konstruktor: buat storage kosong untuk graph
        self.adj_list = {}  # Gunakan dictionary untuk menyimpan hubungan antar node
        self.directed = directed  # Simpan apakah graph directed (satu arah) atau tidak
    
def add_vertex(self, v):  # Fungsi untuk menambah node baru
        if v not in self.adj_list:  # Cek apakah node sudah ada
            self.adj_list[v] = []  # Jika belum ada, buat list kosong untuk tetangganya
    
    def add_edge(self, u, v, weight=None):  # Fungsi untuk membuat hubungan antar node
        self.add_vertex(u)  # Pastikan node u sudah ada
        self.add_vertex(v)  # Pastikan node v sudah ada
        if v not in self.adj_list[u]:  # Cek agar tidak ada duplikat hubungan
            self.adj_list[u].append(v)  # Tambah v ke list tetangga u
        if not self.directed and u not in self.adj_list[v]:  # Jika undirected, tambah balik
            self.adj_list[v].append(u)  # Tambah u ke list tetangga v
    
    def remove_edge(self, u, v):  # Fungsi untuk menghapus hubungan antar node
        if u in self.adj_list and v in self.adj_list[u]:  # Cek apakah hubungan u→v ada
            self.adj_list[u].remove(v)  # Hapus v dari list tetangga u
        if not self.directed and v in self.adj_list and u in self.adj_list[v]:  # Jika undirected
            self.adj_list[v].remove(u)  # Hapus hubungan v→u juga
    
    def has_edge(self, u, v):  # Fungsi untuk cek apakah ada hubungan u ke v
        return u in self.adj_list and v in self.adj_list[u]  # Return True jika v adalah tetangga u
    
    def get_neighbors(self, v):  # Fungsi untuk mendapat semua tetangga dari node v
        return self.adj_list.get(v, [])  # Return list tetangga, atau [] jika v tidak ada
    
    def get_vertices(self):  # Fungsi untuk mendapat semua node dalam graph
        return list(self.adj_list.keys())  # Return list semua key/node dari dictionary
    
    def get_edge_count(self):  # Fungsi untuk hitung total hubungan
        total = sum(len(neighbors) for neighbors in self.adj_list.values())  # Jumlah tetangga semua node
        return total if self.directed else total // 2  # Jika undirected, bagi 2 (karena dihitung 2x)
    
    def degree(self, v):  # Fungsi untuk hitung berapa banyak tetangga node v
        return len(self.adj_list.get(v, []))  # Return jumlah tetangga v
    
    def display(self):  # Fungsi untuk tampilkan adjacency list
        """Menampilkan adjacency list"""
        print("\nAdjacency List:")  # Tampilkan judul
        for vertex in sorted(self.adj_list.keys()):  # Loop untuk setiap node
            neighbors = sorted(self.adj_list[vertex])  # Urutkan tetangga
            print(f"  {vertex}: {neighbors}")  # Tampilkan node dan tetangganya


class GraphAdjMatrix:  # Kelas untuk membuat graph menggunakan matrix 2D
    def __init__(self, vertices, directed=False):  # Konstruktor: setup matrix dan simpan info node
        self.vertices = vertices  # Simpan nama semua node (mis: ['A','B','C'])
        self.n = len(vertices)  # Hitung jumlah node untuk ukuran matrix
        self.vertex_index = {v: i for i, v in enumerate(vertices)}  # Buat mapping nama→index
        self.matrix = [[0] * self.n for _ in range(self.n)]  # Buat matrix 2D berisi 0 (belum ada hubungan)
        self.directed = directed  # Simpan apakah graph directed atau undirected
    
    def add_edge(self, u, v, weight=1):  # Fungsi untuk membuat hubungan antar node
        i, j = self.vertex_index[u], self.vertex_index[v]  # Konversi nama node menjadi index matrix
        self.matrix[i][j] = weight  # Set nilai 1 di posisi (i,j) untuk tandai ada hubungan
        if not self.directed:  # Jika undirected, tambahkan hubungan sebaliknya
            self.matrix[j][i] = weight  # Set nilai 1 di posisi (j,i) juga
    
    def has_edge(self, u, v):  # Fungsi untuk cek apakah ada hubungan u ke v
        i, j = self.vertex_index[u], self.vertex_index[v]  # Konversi nama ke index
        return self.matrix[i][j] != 0  # Jika nilai ≠ 0, berarti ada hubungan
    
    def get_neighbors(self, v):  # Fungsi untuk cari semua tetangga node v
        idx = self.vertex_index[v]  # Konversi nama node ke index
        return [self.vertices[j] for j in range(self.n) if self.matrix[idx][j] != 0]  # Return nama node yang terhubung

    
    def display(self):  # Fungsi untuk tampilkan matrix secara visual
        """Menampilkan adjacency matrix"""
        print("\nAdjacency Matrix:")  # Tampilkan judul
        header = "    " + "  ".join(f"{v:>3}" for v in self.vertices)  # Buat header dengan nama node
        print(header)  # Tampilkan header
        for i, v in enumerate(self.vertices):  # Loop untuk setiap baris (setiap node)
            row = "  ".join(f"{self.matrix[i][j]:>3}" for j in range(len(self.vertices)))  # Buat satu baris matrix
            print(f"  {v:>3} {row}")  # Tampilkan nama node dan isi baris
    