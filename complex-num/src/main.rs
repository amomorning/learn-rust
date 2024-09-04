use num::complex::Complex;

fn main() {
    let a = Complex {re: 2.1, im: -1.2};
    let b = Complex::new(3.1, 4.2);
    let result = a + b;
    println!("The result is: {}", result);
}
