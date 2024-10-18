# TODO Найдите количество книг, которое можно разместить на дискете

disk_size_mb = 1.44
pages_per_book = 100
lines_per_page = 50
chars_per_line = 25
bytes_per_char = 4

bytes_per_kb = 1024
kb_per_mb = 1024
disk_size_bytes = disk_size_mb * kb_per_mb * bytes_per_kb

book_size_bytes = pages_per_book * lines_per_page * chars_per_line * bytes_per_char

books_on_disk = disk_size_bytes // book_size_bytes

print("Количество книг, помещающихся на дискету:", int(books_on_disk))
