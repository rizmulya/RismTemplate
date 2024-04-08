from RismTemplate import ReactaLaraGenerator


reacta = ReactaLaraGenerator()

reacta.set_template("index", "testing.rism")

data = {
    'name': 'User',
    'fields': ['name', 'email'],
}

if __name__ == "__main__":
    reacta.make_page("index", data)
