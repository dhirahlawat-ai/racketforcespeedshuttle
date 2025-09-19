# Constants
mass = 0.00475  
drag_coefficient = 0.8  
area = 0.0095  
air_density = 1.225  

force = float(input("Enter the force applied by racket (in Newtons): "))
contact_time = 0.003 

# Impulse: F * Δt = m * Δv --> Δv = F * Δt / m
delta_v = force * contact_time / mass
v_initial = delta_v
v_initial = v_initial * 18 / 5

print("\n----- Shuttlecock Speed Summary -----")
print(f"Mass of shuttlecock: {mass*1000:.2f} g")
print(f"Force applied: {force:.2f} N")
print(f"Contact time: {contact_time*1000:.1f} ms")
print(f"Maximum speed achieved: {v_initial:.2f} km/h")
print("-------------------------------------")
