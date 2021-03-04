{
    'name': 'Product Container Deposit',
    'summary': 'Container products e.g. bottles on products and sales orders',
    'author': 'Onestein',
    'license': 'AGPL-3',
    'website': 'https://onestein.nl',
    'category': 'Sales',
    'version': '14.0.1.0.0',
    'depends': [
        'product',
        'sale',
        'account'
    ],
    'data': [
        'views/product_template_view.xml',
        'views/sale_order_view.xml',
        'views/account_move_view.xml',
        'views/account_account_view.xml',
        'reports/report_saleorder.xml',
        'reports/report_invoice.xml'
    ]
}
