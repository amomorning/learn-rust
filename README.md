# learn-rust

[Official Docs](https://doc.rust-lang.org/book/foreword.html)
[Rust Course](https://course.rs/about-book.html)
[Rust by Practice](https://practice-zh.course.rs/)

## Basic

### CLI tools

``` bash
# new project
cargo new guessing_game
cd guessing_game

# run project
cargo run --release

# run with input file
cargo run < main.in

# build project
cargo build --release

# check (Quickly verify if it can be compiled)
cargo check

```

### `Cargo.toml` 和 `Cargo.lock`

`Cargo.toml`是`cargo`特有的**项目数据描述文件**。它存储了项目的所有元配置信息。

`Cargo.lock` 文件是 `cargo` 工具根据同一项目的 `toml` 文件生成的**项目依赖详细清单**。

如果项目是可运行程序`bin`，那么需要将`Cargo.lock`上传到git仓库，如果是依赖库项目`lib`，则需要添加到`.gitignore`当中。

#### configs

``` toml
[package]
name = "basic"
version = "0.1.0"
edition = "2021"
```

#### dependencies

根据依赖项的来源可以分为：

1. Rust 官方库 `crates.io`，通过版本说明来描述
2. 项目的 git 仓库地址，通过 URL 来描述
3. 基于本地项目的绝对路径或者相对路径，通过类 Unix 模式的路径来描述

``` toml
[dependencies]
rand = "0.3"
hammer = { version = "0.5.0"}
color = { git = "https://github.com/bjz/color-rs" }
geometry = { path = "crates/geometry" }
```

## collections

[std::collections](https://doc.rust-lang.org/std/collections/index.html)
