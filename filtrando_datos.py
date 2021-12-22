DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]


def run():
    #Filtrado usando list_comprehensions
    all_python_devs = [worker["name"] for worker in DATA if worker["language"] == 'python']
    all_platzi_workers = [worker['name'] for worker in DATA if worker['organization'] == 'Platzi']

    #Creación de las funciones con map y filter
    adults = list(filter(lambda worker: worker['age'] > 18, DATA))
    adults = list(map(lambda worker: worker["name"], adults))
    
    old_people = list(map(lambda worker: worker | {'old': worker['age'] > 70}, DATA))

    #Reto: Recrear las funciones creadas con list_comprehensions usando filter y map
    all_python_devs_sup_ord_func = list(filter(lambda worker: worker['language'] == 'python', DATA))
    all_python_devs_sup_ord_func = list(map(lambda worker: worker['name'], all_python_devs_sup_ord_func))

    all_platzi_workers_sup_ord_func = list(filter(lambda worker: worker['organization'] == 'Platzi', DATA))
    all_platzi_workers_sup_ord_func = list(map(lambda worker: worker['name'], all_platzi_workers_sup_ord_func))

    #Reto: Recrear la función creada con filter y map usando list_comprehensions 

    adults_list_comp = [worker['name'] for worker in DATA if worker['age'] > 18]
    old_people_comp = [worker | {'old': worker['age'] > 70} for worker in DATA]

    for worker in old_people_comp:
        print(worker)


if __name__ == "__main__":
    run()