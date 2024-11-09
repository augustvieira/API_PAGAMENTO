import mercadopago

def gerar_link_pagamento():
    sdk = mercadopago.SDK("APP_USR-4755249856952424-110122-4f10ca879ee73289791202a8b1ff8e17-2070356881")

    request_options = mercadopago.config.RequestOptions()
    request_options.custom_headers = {
        'x-idempotency-key': '<SOME_UNIQUE_VALUE>'
    }

    payment_data = {
        "items": [
            {
                "id": "1",
                "title": "Camisa",
                "quantity": 1,
                "currency_id": "BRL",
                "unit_price": 259.99
            }
        ],
        "back_urls": {
            "success": "http://127.0.0.1:5500/templates/compracerta.html",
            "failure": "http://127.0.0.1:5500/templates/compraerrada.html",
            "pending": "http://127.0.0.1:5500/templates/compraerrada.html",
        },
        "auto_return": "all"
    }

    result = sdk.preference().create(payment_data, request_options)
    payment = result["response"]
    link_iniciar_pagamento = payment["init_point"]
    
    return link_iniciar_pagamento



