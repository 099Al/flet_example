import time

import flet as ft
from flet_route import Params, Basket
from utils.style import *
from utils.validation import Validation


class SignupPage:
    validation = Validation()

    error_field = ft.Text(' ', color='red')
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

    login_input = ft.Container(
        content=ft.TextField(
            label="Укажите логин",
            bgcolor=secondaryBgColor,
            border=ft.InputBorder.NONE,
            filled=True,
            color=secondaryFontColor,
        ),
        border_radius=15,
    )

    password_input = ft.Container(
        content=ft.TextField(
            label="Пароль",
            password=True,
            can_reveal_password=True,
            bgcolor=secondaryBgColor,
            border=ft.InputBorder.NONE,
            filled=True,
            color=secondaryFontColor,
        ),
        border_radius=15,
    )

    password_confirm = ft.Container(
        content=ft.TextField(
            label="Подтвердите пароль",
            password=True,
            can_reveal_password=True,
            bgcolor=secondaryBgColor,
            border=ft.InputBorder.NONE,
            filled=True,
            color=secondaryFontColor,
        ),
        border_radius=15,
    )

    def display_error(self, message, input_field=None, highlight_input=False):
        """Helper function to display error messages."""
        if highlight_input and input_field:
            input_field.content.bgcolor = inputBgErrorColor
            input_field.update()

        self.error_field.value = message
        self.error_field.size = 12
        self.error_field.update()

        # Wait and reset error display
        time.sleep(1)
        self.error_field.size = 0      # скрыть сообщение
        self.error_field.update()

        if highlight_input and input_field:
            input_field.content.bgcolor = inputBgColor
            input_field.update()

    def view(self, page: ft.Page, params: Params, basket: Basket):
        page.title = "Страница Регистрации"
        page.window.width = defaultWidthWindow
        page.window.height = defaultWidthWindow
        page.window.min_width = 800
        page.window.min_height = 400
        page.fonts = {"cuprum": "fonts/Cuprum.ttf"}

        def signup(e):
            email_value = self.email_input.content.value
            login_value = self.login_input.content.value
            password_value = self.password_input.content.value
            password_confirm = self.password_confirm.content.value
            if email_value and login_value and password_value and password_confirm:
                if not self.validation.is_valid_email(email_value):
                    self.display_error('поле Email не соответствует формату',
                                       input_field=self.email_input,
                                       highlight_input=True)
                elif not self.validation.is_valid_password(password_value):
                    self.display_error('пароль должен быть более 5 символов содержать минимуи 1 спец.символ',
                                       input_field=self.password_input,
                                       highlight_input=True)
                elif password_value != password_confirm:
                    self.display_error('пароли не совпадают',
                                       input_field=self.password_confirm,
                                       highlight_input=True)
                else:
                    self.error_field.value = 'Вы успешно зарегистрированы'
                    self.error_field.size = 12
                    self.error_field.color = ft.colors.GREEN
                    self.error_field.update()
                    time.sleep(4)
                    page.go('/')
            else:
                self.display_error('Заполните все поля',
                                   input_field=None,
                                   highlight_input=False)
            #print(email_value, login_value, password_value)



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
                                        "Регистрация",
                                        color=defaultFontColor,
                                        size=25,
                                        weight=ft.FontWeight.NORMAL,
                                        font_family='cuprum'
                                    ),
                                    self.error_field,
                                    self.login_input,
                                    self.email_input,
                                    self.password_input,
                                    self.password_confirm,

                                    ft.Container(
                                        ft.Text("Зарегистрироваться", color=defaultFontColor),
                                        alignment=ft.alignment.center,
                                        height=40,
                                        bgcolor=hoverBgcolor,
                                        on_click=lambda e: signup(e)
                                    )
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
                                        name=ft.icons.VERIFIED_USER_ROUNDED,  #встроенные иконки
                                        color=hoverBgcolor,
                                        size=140,
                                    ),
                                    ft.Text(
                                        "Форма регистрации",
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
    # def signup(self, e, page: ft.Page):
