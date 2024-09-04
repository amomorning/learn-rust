fn add(x: i32, y: i32) -> i32 {
    x + y
}


fn main() {
    let a = 10;
    let b: i32 = 20;

    let (mut c, d) = (30_i32, 40_i32);
    let e = add(add(a, b), add(c, d));
    c = 50;
    println!("The value of c is: {}", c);

    println!("The value of e is: {}", e);
}

