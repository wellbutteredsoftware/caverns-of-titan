// Super basic sound player and manager
//

use std::path::Path;
use macroquad::audio::*;

/// This assumes that all sound assets are WAVs... which they are
fn get_asset_file(file: &str) -> bool {
    return Path::new(&format!("{}.wav", file)).exists();
}

pub async fn stream_audio(sound_name: &str) {
    if !get_asset_file(&sound_name) {
        println!("Failed to find asset: {} !", sound_name);
        return;
    }
    
    match load_sound(sound_name).await {
        Ok(sound) => {
            play_sound_once(&sound);
        }
        Err(e) => {
            println!("Failed to load asset: {}.wav!", sound_name);
        }
    }
}