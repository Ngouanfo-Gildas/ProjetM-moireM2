/*********************************************
 * OPL 12.9.0.0 Model
 * Author: ngouanfo-G
 * Creation Date: Feb 8, 2022 at 3:10:17 PM
 * Description: 
 *********************************************/
// Paramètre du modèle
 int N = ...;   		// nombre de positions potentielles
 int M = ...;    		// nombre de sources de pollution
 int K = ...;    		// nombre de zones de pollution
 int s = ...;    		// nombre de nombre de scénarios météorologiques
 int z = ...;    		// nombre de nombre de scénarios météorologiques
 
 range p_potentiel = 1..N; 
 range p_pollution = 1..M; 
 range scenario    = 1..s; 
 range zones       = 1..z; 
 
 int    P[p_potentiel] = ...; 		// ensemble de positions potentielles
 float  I[p_pollution] = ...; 		// ensemble des sources de pollution
 float  S[scenario]    = ...; 		// Ensemble des scénarios météorologiques
 float  Z_i_s[zones]   = ...; 	    // Ensemble des zones de pollution
 
 int   costSensor = ...;  // coût d'un noeud de capteurs
 float W_ip_s = ...; 	  //sensibilité du capteur
 float beta = ...; 
 float t_i_s = ...;
 float sigma = ...;
 
 // Variables de décision
 dvar boolean x[p_potentiel];
 
// fonction objectif 
 dexpr int cost = sum(p in p_potentiel) x[p]*costSensor;

//modèles 
minimize cost;
subject to {
	// contraintes
	const01: // contrainte 1
	forall (p in p_potentiel) 
	  sum(s in scenario) t_i_s >= sigma;
	
	const02: // contrainte 2
	forall (i in p_pollution)
	forall (s in scenario)
	  sum(p in zones) x[p]*log(1-W_ip_s) <= t_i_s * log(1-beta);
}
 