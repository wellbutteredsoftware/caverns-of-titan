mod player;

use macroquad::prelude::*;
use crate::player::Player;

#[macroquad::main("Caverns of Titan")]
async fn main() {
    
    // Game and utility initalizing
    let mut plr = Player::new(
        screen_width() / 2.0, 
        screen_height() / 2.0, 
        32.0, 64.0, 200.0, 
        400.0, "default".to_string()).await;

    loop {
        clear_background(BLACK);

        plr.update();

        plr.draw();

        next_frame().await
    }
}