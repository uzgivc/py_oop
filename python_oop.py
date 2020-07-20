#TestRail client

class TestRunBuilder:
    url = "https://react-redux.realworld.io"

    def __init__(self, first_name, last_name, user_email, user_password):
        self.name = first_name
        self.second_name = last_name
        if "@" in user_email:
            self.email = user_email
        else:
            print('Invalid email, enter with @')
        self.password = user_password

    def registration_test_suite(self):
            print("----------------------")
            print("Registration_suite: ")
            print("Go to 'Sign up' page")
            print(f"Enter name in the field as {self.name}")
            print(f"Enter user_email in the field as {self.email}")
            print(f"Enter user_password in the field as {self.password}")
            print("Push [Sign In] button")
            print("Check redirection on main page")

    def login_flow (self):
        print("----------------------")
        print("Go to 'Sign In' page")
        print(f"Enter user_email in the field as {self.email}")
        print(f"Enter user_password in the field as {self.password}")
        print("Push [Sign In] button")
        print("Check redirection on main page")

    def login_test_suite (self):
        print("----------------------")
        print("Login_suite: ")
        self.login_flow()


    def article_create_flow (self):

        print("----------------------")
        print("Article_suite: ")
        self.login_flow()
        print("Click on 'New Post' link")
        print("Fill all fields with 'test_message'")
        print("Push [Publish Article] button")
        print("Check redirection on article page")

    def test_run_smoke(self):
        print("----------------------")
        print("It is Smoke testing!")
        self.login_test_suite()
        self.registration_test_suite()
    def test_run_sanity(self):
        print("----------------------")
        print("It is Sanity testing!")
        self.article_create_flow()
    def test_run_regression(self):
        print("----------------------")
        print("It is Regression testing!")
        self.registration_test_suite()
        self.login_test_suite()
        self.article_create_flow()

test_run= TestRunBuilder("Scarlett", "Johansson", "Scarlett@gmail.com", 187654321)
test_run.test_run_smoke()
test_run.test_run_sanity()
test_run.test_run_regression()


