package com.mycompany.bfs2;

import java.util.LinkedList;
import java.util.List;


public class Vertex <T> {
    private final T data;
    private boolean visited;
    private List<Vertex<T>> links = new LinkedList<>();

    void setNeighbors(List<Vertex<T>> of) {
        this.links=of;
    }
    
    /*
     * @return
     */
    public List<Vertex<T>> getNeighbors(){
        return this.links;   
    }

    public Vertex(T data) {
        this.data = data;
    }
    
    public void setVisited(boolean v){
        this.visited=v;
    }
    
    public boolean isVisited(){
        return visited;
    }
    
}
