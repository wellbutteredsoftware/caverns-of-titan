use macroquad::prelude::*;

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