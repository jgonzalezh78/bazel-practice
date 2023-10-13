package com.jogz78.javagreeter.main;

import com.jogz78.javagreeter.greeter.Greeter;

public class Main {
    public static void main(String args[]) {
        Greeter greeter = new Greeter();
        System.out.println(String.format( " %s",greeter.greet()));
    }
}