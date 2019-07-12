nama = 'joko'
daftar_nama=['saya', 'aku', 'i', 'myself']
print(daftar_nama)
daftar_nama.append('kulo')
daftar_nama.append('abdi')
print(daftar_nama)

for dn in daftar_nama:
    print('Nama lain anda adalah %s, padahal nama aslimu it %s lho' % (dn, nama))
