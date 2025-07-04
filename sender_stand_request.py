
import configuration
import data
import requests



def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
			# inserta la dirección URL completa
                         json=body,  # inserta el cuerpo de solicitud
                         headers=data.headers)  # inserta los encabezados

response = post_new_user(data.user_body)
assert response.status_code == 201, f"Hubo un error {response.status_code}. Verifica la peticion"
print(response.status_code)
print(response.json()['authToken'])




def post_new_client_kit (kit_body, auth_token):
    headers_dict = data.headers.copy()
    headers_dict ["Authorization"] = "Bearer" + auth_token
    return requests.post(configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH,
        # Concatenación de URL base y ruta.
                             json=kit_body, # Datos a enviar en la solicitud.
                             headers=headers_dict)




def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)


