mod player;

use macroquad::prelude::*;
use crate::player::Player;

pub struct Room {
    pub id: String,
    pub size: Vec2,
    pub bg_colour: Color,
    pub exits: Vec<Exit>,
    pub tiles: Vec<Tile>,
}

pub struct Exit {
    pub points_to: String,
    pub pos: Vec2,
}

pub struct Tile {
   
}

pub enum TileKind {
    Solid,
    Platform,
    Ice,
}

#[derive(Debug, Clone, Copy, PartialEq, Eq, Hash)]
pub enum Rooms {
    
}

/// TODO: Functions to init rooms, load and verify them, etc.

fn verify_room_toml(room: &String) {}

/// To be used when an Exit tile is walked on or triggered.
/// Simply warps the player to the provided RoomID.
pub fn change_room(room_id: &String, player: &Player) {
    if player.current_room == room_id {
        println!("Err: Player pos: {} is the same as dest: {}", player.current_room, room_id);
    }

    /// Setup a small transition for movement between rooms
    /// possibly maintaining physics to avoid feeling janky?
}

/// Batch inits all the rooms it can find in the `./assets/rooms` dir.
/// May hitch occasionally on web builds or low end machines.
pub fn init_room_batch() {

}