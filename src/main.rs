mod player;
mod audio;

use macroquad::prelude::*;
use crate::player::Player;
use crate::audio::stream_audio;

#[macroquad::main("Caverns of Titan")]
async fn main() {
    
    // Game and utility initalizing
    let mut plr = Player::new(screen_width() / 2.0, screen_height() / 2.0, 32.0, 32.0, 200.0);

    stream_audio("intro").await;
    loop {
        clear_background(BLACK);

        plr.update();

        plr.draw();

        next_frame().await
    }
}