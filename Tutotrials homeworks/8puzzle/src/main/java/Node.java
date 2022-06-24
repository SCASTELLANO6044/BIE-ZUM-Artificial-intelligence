import java.io.*;
import java.util.HashMap;

public class Node {
    private int[] state;
    private int hDisplaced;
    private int hManhattan;
    private int gVal;
    private HashMap<String,Node> children = new HashMap<String, Node>();
    private Node parentNode;
    private String parentAction;

    public Node(){

    }

    public Node(int[]inState){
        this.state= inState;
        this.gVal=0;
        this.parentNode=null;
        this.parentAction=null;
    }
    public boolean equalState(Node s1, Node s2){
        if (s1.state == s2.state){
            return true;
        }else {
            return false;
        }
    }

    public void expand(){
        int blankPos=0;
        for (int i=0;i<this.state.length;i++){
            if (this.state[i]==0){
                blankPos = i;
            }
        }

        if (blankPos==0){
            int [] rightArray = this.state.clone();
            rightArray[0]=rightArray[1];
            rightArray[1]=0;

            Node right = new Node(rightArray);
            right.setParentAction("right");
            right.setParentNode(this);
            right.calc_hDisplaced();
            right.calc_hManhattan();
            right.setgVal(right.getParentNode().getVal()+1);

            this.children.put("right", right);
            this.children.put("down", down);
        } else if(blankPos==1){
            int [] leftArray = this.state.clone();
            leftArray[1]=leftArray[0];
            leftArray[0]=0;

            Node left = new Node(leftArray);
            left.setParentAction("left");
            left.setParentNode(this);
            left.calc_hDisplaced();
            left.calc_hManhattan();
            left.setgVal(left.getParentNode().getVal()+1);

            int[] rightArray = this.state.clone();
            rightArray[1]=rightArray[2];
            rightArray[2]=0;

            Node right = new Node(rightArray);
            right.setParentAction("right");
            right.setParentNode(this);
            right.calc_hDisplaced();
            right.calc_hManhattan();
            right.setgVal(right.getParentNode().getVal()+1);

            int[] downArray = this.state.clone();
            downArray[1]=downArray[4];
            downArray[4]=0;

            Node down = new Node(downArray);
            down.setParentAction("down");
            down.setParentNode(this);
            down.calc_hDisplaced();
            down.calc_hManhattan();
            down.setgVal(down.getParentNode().getVal()+1);

            this.children.put("right", right);
            this.children.put("down", down);
            this.children.put("left", left);
        } else if (blankPos == 2){
            int [] leftArray = this.state.clone();
            leftArray[2]=leftArray[1];
            leftArray[1]=0;

            Node left = new Node(leftArray);
            left.setParentAction("left");
            left.setParentNode(this);
            left.calc_hDisplaced();
            left.calc_hManhattan();
            left.setgVal(left.getParentNode().getVal()+1);

            int[] downArray = this.state.clone();
            downArray[2]=downArray[5];
            downArray[5]=0;

            Node down = new Node(downArray);
            down.setParentAction("down");
            down.setParentNode(this);
            down.calc_hDisplaced();
            down.calc_hManhattan();
            down.setgVal(down.getParentNode().getVal()+1);

            this.children.put("down", down);
            this.children.put("left", left);
        } else if (blankPos == 3){
            int upArray = this.state.clone();
            upArray[3]=upArray[0];
            upArray[0]=0;

            Node up = new Node(upArray);
            up.setParentAction("up");
            up.setParentNode(this);
            up.calc_hDisplaced();
            up.calc_hManhattan();
            up.setgVal(up.getParentNode().getVal()+1);

            int[] rightArray = this.state.clone();
            rightArray[3]=rightArray[4];
            rightArray[4]=0;

            Node right = new Node(rightArray);
            right.setParentAction("right");
            right.setParentNode(this);
            right.calc_hDisplaced();
            right.calc_hManhattan();
            right.setgVal(right.getParentNode().getVal()+1);

            int[] downArray = this.state.clone();
            downArray[3]=downArray[6];
            downArray[6]=0;

            Node down = new Node(downArray);
            down.setParentAction("down");
            down.setParentNode(this);
            down.calc_hDisplaced();
            down.calc_hManhattan();
            down.setgVal(down.getParentNode().getVal()+1);

            this.children.put("right",right);
            this.children.put("down",down);
            this.children.put("up",up);
        } else if (blankPos==4){
            int [] leftArray = this.state.clone();
            leftArray[4]=leftArray[3];
            leftArray[3]=0;

            Node left = new Node(leftArray);
            left.setParentAction("left");
            left.setParentNode(this);
            left.calc_hDisplaced();
            left.calc_hManhattan();
            left.setgVal(left.getParentNode().getVal()+1);

            int upArray = this.state.clone();
            upArray[4]=upArray[1];
            upArray[1]=0;

            Node up = new Node(upArray);
            up.setParentAction("up");
            up.setParentNode(this);
            up.calc_hDisplaced();
            up.calc_hManhattan();
            up.setgVal(up.getParentNode().getVal()+1);

            int[] rightArray = this.state.clone();
            rightArray[4]=rightArray[5];
            rightArray[5]=0;

            Node right = new Node(rightArray);
            right.setParentAction("right");
            right.setParentNode(this);
            right.calc_hDisplaced();
            right.calc_hManhattan();
            right.setgVal(right.getParentNode().getVal()+1);

            int[] downArray = this.state.clone();
            downArray[4]=downArray[7];
            downArray[7]=0;

            Node down = new Node(downArray);
            down.setParentAction("down");
            down.setParentNode(this);
            down.calc_hDisplaced();
            down.calc_hManhattan();
            down.setgVal(down.getParentNode().getVal()+1);

            this.children.put("right",right);
            this.children.put("down",down);
            this.children.put("up",up);
            this.children.put("left",left);
        } else if (blankPos = 5){
            int [] leftArray = this.state.clone();
            leftArray[5]=leftArray[4];
            leftArray[4]=0;

            Node left = new Node(leftArray);
            left.setParentAction("left");
            left.setParentNode(this);
            left.calc_hDisplaced();
            left.calc_hManhattan();
            left.setgVal(left.getParentNode().getVal()+1);

            int upArray = this.state.clone();
            upArray[5]=upArray[2];
            upArray[2]=0;

            Node up = new Node(upArray);
            up.setParentAction("up");
            up.setParentNode(this);
            up.calc_hDisplaced();
            up.calc_hManhattan();
            up.setgVal(up.getParentNode().getVal()+1);

            int[] downArray = this.state.clone();
            downArray[5]=downArray[8];
            downArray[8]=0;

            Node down = new Node(downArray);
            down.setParentAction("down");
            down.setParentNode(this);
            down.calc_hDisplaced();
            down.calc_hManhattan();
            down.setgVal(down.getParentNode().getVal()+1);

            this.children.put("down",down);
            this.children.put("up",up);
            this.children.put("left",left);
        } else if (blankPos == 6){
            int upArray = this.state.clone();
            upArray[6]=upArray[3];
            upArray[3]=0;

            Node up = new Node(upArray);
            up.setParentAction("up");
            up.setParentNode(this);
            up.calc_hDisplaced();
            up.calc_hManhattan();
            up.setgVal(up.getParentNode().getVal()+1);

            int[] rightArray = this.state.clone();
            rightArray[6]=rightArray[7];
            rightArray[7]=0;

            Node right = new Node(rightArray);
            right.setParentAction("right");
            right.setParentNode(this);
            right.calc_hDisplaced();
            right.calc_hManhattan();
            right.setgVal(right.getParentNode().getVal()+1);

            this.children.put("right",right);
            this.children.put("up",up);
        } else if(blankPos == 7){
            int [] leftArray = this.state.clone();
            leftArray[7]=leftArray[6];
            leftArray[6]=0;

            Node left = new Node(leftArray);
            left.setParentAction("left");
            left.setParentNode(this);
            left.calc_hDisplaced();
            left.calc_hManhattan();
            left.setgVal(left.getParentNode().getVal()+1);

            int upArray = this.state.clone();
            upArray[7]=upArray[4];
            upArray[4]=0;

            Node up = new Node(upArray);
            up.setParentAction("up");
            up.setParentNode(this);
            up.calc_hDisplaced();
            up.calc_hManhattan();
            up.setgVal(up.getParentNode().getVal()+1);

            int[] rightArray = this.state.clone();
            rightArray[7]=rightArray[8];
            rightArray[8]=0;

            Node right = new Node(rightArray);
            right.setParentAction("right");
            right.setParentNode(this);
            right.calc_hDisplaced();
            right.calc_hManhattan();
            right.setgVal(right.getParentNode().getVal()+1);

            this.children.put("right",right);
            this.children.put("up",up);
            this.children.put("left",left);
        } else if (blankPos == 8){
            int [] leftArray = this.state.clone();
            leftArray[8]=leftArray[7];
            leftArray[7]=0;

            Node left = new Node(leftArray);
            left.setParentAction("left");
            left.setParentNode(this);
            left.calc_hDisplaced();
            left.calc_hManhattan();
            left.setgVal(left.getParentNode().getVal()+1);

            int upArray = this.state.clone();
            upArray[8]=upArray[5];
            upArray[5]=0;

            Node up = new Node(upArray);
            up.setParentAction("up");
            up.setParentNode(this);
            up.calc_hDisplaced();
            up.calc_hManhattan();
            up.setgVal(up.getParentNode().getVal()+1);

            this.children.put("up",up);
            this.children.put("left", left);
        } else {

        }
    }

    public void calc_hDisplaced(){
        int sum = 0;
        if (this.state[0]!=1){
            sum++;
        }
        if (this.state[1]!=2){
            sum++;
        }
        if (this.state[2]!=3){
            sum++;
        }
        if (this.state[3]!=8){
            sum++;
        }
        if (this.state[4]!=0){
            sum++;
        }
        if (this.state[5]!=4){
            sum++;
        }
        if (this.state[6]!=7){
            sum++;
        }
        if (this.state[7]!=6){
            sum++;
        }
        if (this.state[8]!=5){
            sum++;
        }
        this.setDisplaced(sum);
    }

    public void calc_hManhattan(){
        int sum = 0;
        if (this.state[0]!=1){
            if(this.state[1]==1||this.state[3]==1){
                sum+=1;
            } else if (this.state[2]==1||this.state[4]==1||this.state[6]==1){
                sum+=2;
            } else if (this.state[5]==1||this.state[7]==1){
                sum+=3;
            } else if (this.state[8]==1){
                sum+=4;
            }
        }

        if (this.state[1]!=2){
            if(this.state[0]==2||this.state[4]==2 || this.state[2]==2){
                sum+=1;
            } else if (this.state[3]==2||this.state[5]==2||this.state[6]==2){
                sum+=2;
            } else if (this.state[6]==2||this.state[8]==2){
                sum+=3;
            }
        }
    }

}
