import {Canvas, useFrame} from '@react-three/fiber';
import {OrbitControls} from '@react-three/drei';
import { useRef } from 'react';

const RotatingCube = () => {
  const meshRef = useRef(null);
  useFrame(() => {
    if (meshRef.current) {
      meshRef.current.rotation.x += 0.01;
      meshRef.current.rotation.y += 0.01;       
    }
  });
  return (
    <mesh ref={meshRef}>
      <cylinderGeometry args={[1, 1, 1]} />
      <meshLambardMaterial color="#468585" emissive="#468585" />
    </mesh>
  );
}
const App = () => {
  return (
    <div>
      {/* <h1>Welcome to the 3JS Vite App</h1>
      <p>This is a simple application using Three.js with Vite.</p> */}
      <Canvas style={{ height: '100vh', width: '100vw' , display: 'flex', justifyContent: 'center', alignItems: 'center' }}>
        hello 3js;
        <orbitControls enableZoom enablePan enableRotate />

        <directionalLight position={[1, 1, 1]} intensity={10} color={0x9cdba6} />
        <color attach="background" args={[0xf0f0f0]} />

        <RotatingCube></RotatingCube>
      </Canvas>
    </div>
  );
}

export default App;
