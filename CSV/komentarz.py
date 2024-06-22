# metoda do wgrania .json do bazy danych
#
    # "model": "orm.client",
    #         "pk": 1,       ---   w pliku muszą być kolejne numery
    #         "fields": {
    #             "name": "Innovate Enterprises Inc.",
    #             "slug": "innovate-enterprises-inc",
    #             "address": "321 Pine St, Anytown, USA",
    #             "date": "2024-06-08T20:15:30Z"   ---- data musi być podana pomimo że te pole w bazie danych
#                                                       powinno się samo aktualizować

# folder CSV powinien być w folderze aplikacji a nie folderze root

# komenda terminala
# python manage.py loaddata django_orm_nauka/CSV/orm.json