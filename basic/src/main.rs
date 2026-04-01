use std::cell::Cell;

fn add(x: i32, y: i32) -> i32 {
    x + y
}

fn main() {
    let a = 10;
    let b: i32 = 20;

    let (c, d) = (Cell::new(30_i32), 40_i32);  // c 用 Cell 包装

    let e = || add(add(a, b), add(c.get(), d));  // 通过 get() 读取

    println!("e before: {}", e());  // 100

    c.set(50);  // 通过 set() 修改
    println!("c is: {}", c.get());

    println!("e after: {}", e());  // 120
}
