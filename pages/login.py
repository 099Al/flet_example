import flet as ft
from flet_route import Params, Basket
from utils.style import *


class LoginPage:

    email_input = ft.Container(
        content=ft.TextField(
            label="Укажите Email",
            bgcolor=secondaryBgColor,
            border=ft.InputBorder.NONE,
            filled=True,
            color=secondaryFontColor,
        ),
        border_radius=15,
    )

    password_input = ft.Container(
        content=ft.TextField(
            label="Введите пароль",
            password=True,
            can_reveal_password=True,
            bgcolor=secondaryBgColor,
            border=ft.InputBorder.NONE,
            filled=True,
            color=secondaryFontColor,
        ),
        border_radius=15,
    )

    def view(self, page: ft.Page, params: Params, basket: Basket):
        page.title = "Страница авторизации"
        page.window.width = defaultWidthWindow
        page.window.height = defaultWidthWindow
        page.window.min_width = 800
        page.window.min_height = 400
        page.fonts = {"cuprum": "fonts/Cuprum.ttf"}

        return ft.View(
            "/",
            controls=[
                # ft.Text('Login'),           #элемент с текстов
                # ft.ElevatedButton('Страница регистрации', on_click=lambda e: page.go('/signup')) #кнопка для перехода
                # self.email_input
                ft.Row(
                    expand=True,
                    controls=[
                        ft.Container(
                            expand=2,  # размер контейнера
                            padding=ft.padding.all(40),
                            content=ft.Column(
                                alignment=ft.MainAxisAlignment.CENTER,
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                controls=[
                                    ft.Text(
                                        "Приветствую Вас",
                                        color=defaultFontColor,
                                        size=25,
                                        weight=ft.FontWeight.NORMAL,
                                    ),
                                    self.email_input,
                                    self.password_input,
                                    ft.Container(
                                        ft.Text("Авторизация", color=defaultFontColor),
                                        alignment=ft.alignment.center,
                                        height=40,
                                        bgcolor=hoverBgcolor,
                                    ),
                                    ft.Container(
                                        ft.Text(
                                            "Создать аккаунт", color=defaultFontColor
                                        ),
                                        on_click=lambda e: page.go("/signup"),
                                    ),
                                ],
                            ),
                        ),
                        ft.Container(
                            expand=3,
                            image_src="images/bg_login.jpg",
                            image_fit=ft.ImageFit.COVER,
                            content=ft.Column(
                                alignment=ft.MainAxisAlignment.CENTER,
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                controls=[
                                    ft.Icon(
                                        name=ft.icons.LOCK_PERSON_ROUNDED,
                                        color=hoverBgcolor,
                                        size=140,
                                    ),
                                    ft.Text(
                                        "Авторизация",
                                        color=hoverBgcolor,
                                        size=15,
                                        weight=ft.FontWeight.BOLD,
                                    ),
                                ],
                            ),
                        ),
                    ],
                )
            ],
            bgcolor=defaultBgColor,
            padding=0,
        )
