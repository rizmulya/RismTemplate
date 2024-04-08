from RismTemplate import TemplateProcessor, LaravelGenerator, ReactaLaraGenerator


"""
Example custom

For `flexible customization` of input files, output files, and data
according to your specific requirements.
"""
# data
data = {
    'name': 'User',
    'fields': ['field1', 'field2'],
}

# init
custom = TemplateProcessor()
# generate
custom.render("path/to/input/file", "path/to/output/file", data)


"""
Example ReactaLaraGenerator
Views Generator
https://github.com/rizmulya/reactalara
import from your ReactaLara root direcotry
"""
# init
reacta = ReactaLaraGenerator()
# set_template
reacta.set_template("index", "path/to/index/template")
reacta.set_template("create", "path/to/create/template")
# generate
reacta.make_page("index", data)
reacta.make_page("create", data)


"""
Example LaravelGenerator
Controller Generator
import from your Laravel root direcotry
"""
# init
laravel = LaravelGenerator()
# set_template
laravel.set_template_controller("path/to/controller/template")
# generate
laravel.make_controller(data)
