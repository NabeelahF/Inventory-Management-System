package com.example.myjavafx;
import javafx.application.Application;
import javafx.geometry.Insets;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.layout.GridPane;
import javafx.stage.Stage;

public class RegistrationLoginApp extends Application {
    private Stage primaryStage;
    private Scene registrationScene;
    private Scene loginScene;

    public static void main(String[] args) {
        launch(args);
    }

    @Override
    public void start(Stage primaryStage) {
        this.primaryStage = primaryStage;

        // Create the registration scene
        GridPane registrationGrid = createRegistrationGrid();
        registrationScene = new Scene(registrationGrid, 300, 200);

        // Create the login scene
        GridPane loginGrid = createLoginGrid();
        loginScene = new Scene(loginGrid, 300, 200);

        // Set the initial scene to the registration scene
        primaryStage.setScene(registrationScene);
        primaryStage.setTitle("Registration Page");
        primaryStage.show();
    }

    private GridPane createRegistrationGrid() {
        GridPane grid = new GridPane();
        grid.setPadding(new Insets(10));
        grid.setVgap(10);
        grid.setHgap(10);

        // Registration fields
        Label nameLabel = new Label("Name:");
        TextField nameField = new TextField();
        Label emailLabel = new Label("Email:");
        TextField emailField = new TextField();

        // Register button
        Button registerButton = new Button("Register");
        registerButton.setOnAction(e -> switchToLogin());

        // Add registration components to the grid
        grid.add(nameLabel, 0, 0);
        grid.add(nameField, 1, 0);
        grid.add(emailLabel, 0, 1);
        grid.add(emailField, 1, 1);
        grid.add(registerButton, 0, 2);

        return grid;
    }

    private GridPane createLoginGrid() {
        GridPane grid = new GridPane();
        grid.setPadding(new Insets(10));
        grid.setVgap(10);
        grid.setHgap(10);

        // Login fields
        Label usernameLabel = new Label("Username:");
        TextField usernameField = new TextField();
        Label passwordLabel = new Label("Password:");
        TextField passwordField = new TextField();

        // Login button
        Button loginButton = new Button("Login");
        loginButton.setOnAction(e -> switchToRegistration());

        // Add login components to the grid
        grid.add(usernameLabel, 0, 0);
        grid.add(usernameField, 1, 0);
        grid.add(passwordLabel, 0, 1);
        grid.add(passwordField, 1, 1);
        grid.add(loginButton, 0, 2);

        return grid;
    }

    private void switchToLogin() {
        primaryStage.setScene(loginScene);
        primaryStage.setTitle("Login Page");
    }

    private void switchToRegistration() {
        primaryStage.setScene(registrationScene);
        primaryStage.setTitle("Registration Page");
    }
}
