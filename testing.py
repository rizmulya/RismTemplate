from RismTemplate import ReactaLaraGenerator, TemplateProcessor


data = {
    'name': 'User',
    'fields': ['name', 'email'],
}

# testing 1
custom = TemplateProcessor()
custom.render("testing.rism", "result.someextention", data)

# testing 2
reacta = ReactaLaraGenerator()
reacta.set_template("index", "testing2.rism")
reacta.make_page("index", data)
