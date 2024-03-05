package com.example.myjavafx;

import javafx.fxml.FXML;
import javafx.scene.control.TextField;

public class LoginController {
    @FXML
    private TextField usernameField;

    @FXML
    private TextField passwordField;

    @FXML
    private void loginButtonClicked() {
        // Perform login logic here
        System.out.println("Login Successful");
    }
}
