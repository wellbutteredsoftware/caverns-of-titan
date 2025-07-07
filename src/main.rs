mod player;
mod audio;

use macroquad::prelude::*;
use crate::player::Player;

#[macroquad::main("Caverns of Titan")]
async fn main() {
    
    // Game and utility initalizing

    loop {
        clear_background(BLACK);
        next_frame().await
    }
}