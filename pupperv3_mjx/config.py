from ml_collections import config_dict


def get_config():
    """Returns reward config for barkour quadruped environment.
       I have set all rewards to 0.0 to disable you from looking at the answers!
    """
    def get_default_rewards_config():
        default_config = config_dict.ConfigDict(
            dict(
                # The coefficients for all reward terms used for training. All
                # physical quantities are in SI units (rad, m, Nm, s).
                scales=config_dict.ConfigDict(
                    dict(
                        # Tracking rewards (exp(-err^2 / sigma))
                        tracking_lin_vel=1.5,           # track commanded linear speed
                        tracking_ang_vel=0.8,           # track commanded yaw rate
                        tracking_orientation=3.0,       # match desired body orientation

                        # Base / regularization terms
                        lin_vel_z=-2.0,                 # penalize base vertical velocity
                        ang_vel_xy=-0.05,               # penalize roll/pitch rates
                        orientation=-0.5,               # penalize roll/pitch angles

                        # Torque / dynamics regularizers
                        torques=-0.0002,
                        joint_acceleration=-1e-6,
                        mechanical_work=0.0,

                        # Action smoothness
                        action_rate=-0.01,

                        # Gaits / foot terms
                        feet_air_time=0.2,
                        stand_still= 0.0,
                        stand_still_joint_velocity= 0.0,
                        abduction_angle=-0.1,

                        # Safety / termination
                        termination=-100.0,
                        foot_slip=-0.1,
                        knee_collision=-1.0,
                        body_collision=-1.0,

                        # --- NEW balancing rewards ---
                        # Encourage CoM to be over rear feet support line.
                        com_over_rear=1.0,

                        # Reward for rear foot contacts (encourage rear legs to support load)
                        rear_contact=0.5,

                        # Penalize front foot contact while balancing on rear (negative scale)
                        # Use negative value to penalize front contact.
                        front_contact_penalty=-1.5,
                        front_joint_vel=-0.05,
                        torso_height_reward=5.0,
                    )
                ),
                # Tracking reward width
                tracking_sigma=0.25,
            )
        )
        return default_config

    default_config = config_dict.ConfigDict(
        dict(
            rewards=get_default_rewards_config(),
        )
    )

    return default_config
