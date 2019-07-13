from teman.models import daftar_teman

def run_view():
    print('Daftar Teman')
    print('------------')

    for dt in daftar_teman:
        print(dt)

