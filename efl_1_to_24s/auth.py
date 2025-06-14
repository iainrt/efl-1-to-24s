from services.supabase_client import supabase

def signup_user(email, password):
    return supabase.auth.sign_up({"email": email, "password": password})

def login_user(email, password):
    return supabase.auth.sign_in_with_password({"email": email, "password": password})
