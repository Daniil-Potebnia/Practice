function showPassword(elem) {
    if (!elem.hasAttribute("checked")) {
        elem.setAttribute("checked", "");
        if (elem.getAttribute('name') == "password_again") {
            document.getElementById('password_again').setAttribute("type", "text");
        } else if (elem.getAttribute('name') == "password") {
            document.getElementById('password').setAttribute("type", "text");
        }
    } else {
        elem.removeAttribute("checked");
        if (elem.getAttribute('name') == "password_again") {
            document.getElementById('password_again').setAttribute("type", "password");
        } else if (elem.getAttribute('name') == "password") {
            document.getElementById('password').setAttribute("type", "password");
        }
    }
}

function checkForm(el) {
    login = document.getElementById("login");
    login.setAttribute("class", login.getAttribute("class").replace("focus-ring-danger", "focus-ring-success"));
    login.setAttribute("placeholder", "Логин");

    password = document.getElementById("password");
    password.setAttribute("class", password.getAttribute("class").replace("focus-ring-danger", "focus-ring-success"));
    password.setAttribute("placeholder", "Пароль");

    if (login.value.trim() == "") {
        login.setAttribute("class", login.getAttribute("class").replace("focus-ring-success", "focus-ring-danger"));
        login.setAttribute("placeholder", "Некорректный логин");
        login.focus();
        return false;
    } else if (password.value.trim() == "") {
        password.setAttribute("class", login.getAttribute("class").replace("focus-ring-success", "focus-ring-danger"));
        password.setAttribute("placeholder", "Некорректный пароль");
        password.focus();
        return false;
    }
    if (el.getAttribute("id") == "reg-form") {
        email = document.getElementById("email");
        email.setAttribute("class", password.getAttribute("class").replace("focus-ring-danger", "focus-ring-success"));
        email.setAttribute("placeholder", "Электронная почта");

        repassword = document.getElementById("password_again");
        repassword.setAttribute("class", password.getAttribute("class").replace("focus-ring-danger", "focus-ring-success"));
        repassword.setAttribute("placeholder", "Повторить пароль");

        if (email.value.trim() == "") {
            email.setAttribute("class", login.getAttribute("class").replace("focus-ring-success", "focus-ring-danger"));
            email.setAttribute("placeholder", "Некорректная электронная почта");
            email.focus();
            return false;
        } else if (repassword.value.trim() == "" || repassword.value != password.value) {
            repassword.setAttribute("class", login.getAttribute("class").replace("focus-ring-success", "focus-ring-danger"));
            repassword.setAttribute("placeholder", "Некорректный пароль");
            repassword.focus();
            return false;
        }
    }
    return true;
}
