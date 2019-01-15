import pkg_resources

log_file = pkg_resources.resource_filename(__name__, '../files/{customer}_catalog.json')
print(log_file.format(customer='Hoalen'))
