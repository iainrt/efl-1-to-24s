import flet as ft
from auth import login_user, signup_user
from data.teams_championship import CHAMPIONSHIP_TEAMS_2025_26
from views.home import home_view
from views.prediction import prediction_view

user = None  # store logged-in user

def main(page: ft.Page):
    page.title = "EFL Predictor 2025/26"

    def start_prediction(league):
        if league == "Championship":
            page.clean()
            page.add(prediction_view(page, CHAMPIONSHIP_TEAMS_2025_26, "Championship", user, show_home))

    def show_home():
        page.clean()
        page.add(home_view(start_prediction))

    def handle_login(e):
        global user
        res = login_user(email.value, password.value)
        if res.user:
            user = res.user
            show_home()
        else:
            error.value = "Login failed"
            page.update()

    def handle_signup(e):
        res = signup_user(email.value, password.value)
        if res.user:
            error.value = "Signup successful. Now log in."
        else:
            error.value = res.error.message
        page.update()

    email = ft.TextField(label="Email", width=300)
    password = ft.TextField(label="Password", password=True, width=300)
    error = ft.Text("", color="red")

    page.add(
        ft.Column([
            ft.Text("Login or Sign Up", size=20, weight="bold"),
            email,
            password,
            ft.Row([
                ft.ElevatedButton("Login", on_click=handle_login),
                ft.OutlinedButton("Sign Up", on_click=handle_signup),
            ]),
            error
        ])
    )

ft.app(target=main)
