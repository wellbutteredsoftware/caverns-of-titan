use macroquad::prelude::*;

pub struct Player {
    pub position: Vec2,
    
    #[allow(dead_code)]
    pub direction: Vec2,
    pub size: Vec2,
    pub speed: f32,    
}

impl Player {
    pub fn new(px: f32, py: f32, sx: f32, sy: f32, spd: f32) -> Self {
        Self {
            position: vec2(px, py),
            direction: vec2(0.0,0.0),
            size: vec2(sx, sy),
            speed: spd,
        }
    }

    /// TODO: Implement sprinting and jumping later
    pub fn update(&mut self) {
        if is_key_down(KeyCode::Up) || is_key_down(KeyCode::W) {
            self.position.y -= self.speed * get_frame_time();
        }
        if is_key_down(KeyCode::Down) || is_key_down(KeyCode::S) {
            self.position.y += self.speed * get_frame_time();
        }
        if is_key_down(KeyCode::Left) || is_key_down(KeyCode::A) {
            self.position.x -= self.speed * get_frame_time();
        }
        if is_key_down(KeyCode::Right) || is_key_down(KeyCode::D) {
            self.position.x += self.speed * get_frame_time();
        }

        self.position.y = self.position.y.clamp(0.0, screen_height() - self.size.y);
        self.position.x = self.position.x.clamp(0.0, screen_width() - self.size.x);
    }

    pub fn draw(&self) {
        draw_rectangle(self.position.x, self.position.y, self.size.x, self.size.y, WHITE);
    }

    pub fn rect(&self) -> Rect {
        Rect::new(self.position.x, self.position.y, self.size.x, self.size.y)
    }
}