use macroquad::prelude::*;
use macroquad::audio::*;

pub struct Player {
    pub position: Vec2,
    pub velocity: Vec2,
    pub size: Vec2,
    pub speed: f32,
    pub grounded: bool,
    pub jump_strength: f32,

    // Sound effects
    pub sfx_jump: Option<Sound>,
    pub sfx_bonk: Option<Sound>,
}

impl Player {
    pub async fn new(px: f32, py: f32, sx: f32, sy: f32, spd: f32, jump_strength: f32) -> Self {
        let sfx_jump = load_sound("jump_plr.wav").await.ok();
        let sfx_bonk = load_sound("bonk_plr.wav").await.ok();

        Self {
            position: vec2(px, py),
            velocity: vec2(0.0, 0.0),
            size: vec2(sx, sy),
            speed: spd,
            grounded: false,
            jump_strength,
            sfx_jump,
            sfx_bonk,
        }
    }

    /// TODO: Consider adding ini compatibility for desktop players?
    pub fn update(&mut self) {
        let dt = get_frame_time();
        let mut move_speed = self.speed;

        if is_key_down(KeyCode::LeftShift) || is_key_down(KeyCode::LeftControl) {
            move_speed *= 1.5;
        }
        if is_key_down(KeyCode::Left) || is_key_down(KeyCode::A) {
            self.position.x -= move_speed * dt;
        }
        if is_key_down(KeyCode::Right) || is_key_down(KeyCode::D) {
            self.position.x += move_speed * dt;
        }

        if self.grounded && (is_key_pressed(KeyCode::Space) || is_key_pressed(KeyCode::W)) {
            self.velocity.y = -self.jump_strength;
            self.grounded = false;

            if let Some(snd) = &self.sfx_jump {
                play_sound_once(snd);
            }
        }

        self.velocity.y += 1000.0 * dt;
        self.position += self.velocity * dt;

        let floor_y = screen_height() - self.size.y;
        if self.position.y >= floor_y {
            self.position.y = floor_y;
            self.velocity.y = 0.0;
            if !self.grounded {
                self.grounded = true;
                if let Some(snd) = &self.sfx_bonk {
                    play_sound_once(snd);
                }
            }
        }

        self.position.x = self.position.x.clamp(0.0, screen_width() - self.size.x);
    }

    pub fn draw(&self) {
        draw_rectangle(self.position.x, self.position.y, self.size.x, self.size.y, WHITE);
    }

    pub fn rect(&self) -> Rect {
        Rect::new(self.position.x, self.position.y, self.size.x, self.size.y)
    }
}