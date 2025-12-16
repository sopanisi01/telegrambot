from pyrogram import Client

api_id = 9998249  # Reemplaza con tu API_ID (número)
api_hash = "5bd6be16e8aefa31bc2f9e12435959af"  # Reemplaza con tu API_HASH (cadena)

with Client("mi_sesion", api_id, api_hash) as app:
    print(app.export_session_string())