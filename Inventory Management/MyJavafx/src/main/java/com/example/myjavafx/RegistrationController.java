package com.example.myjavafx;
import javafx.fxml.FXML;
import javafx.scene.control.TextField;

public class RegistrationController {
    @FXML
    private TextField nameField;

    @FXML
    private TextField emailField;

    @FXML
    private void registerButtonClicked() {
        // Perform registration logic here
        System.out.println("Registration Successful");
    }
}
