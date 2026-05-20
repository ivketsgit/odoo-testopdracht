{
    'name': 'Real Estate',
    'version': '18.0.1.0.0',
    'depends': ['base'],
    'author': 'Ian Van Kets',
    'category': 'Real Estate',
    'license': 'LGPL-3',
    'application': True,
    'description': """
    Module for managing real estate properties, including property name, the property type, the postcode and so on. 
    """,
    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        'views/estate_menus.xml',
    ]
}